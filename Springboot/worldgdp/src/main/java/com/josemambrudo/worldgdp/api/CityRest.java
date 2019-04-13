package com.josemambrudo.worldgdp.api;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.josemambrudo.worldgdp.crudRepository.CityRepository;
import com.josemambrudo.worldgdp.entity.City;

import com.josemambrudo.worldgdp.exception.*;

import javax.validation.Valid;

@RestController
public class CityRest {

	@Autowired
	private CityRepository cityRepository;

	@GetMapping("/api/v1/cities")
	public Page<City> getAllCitys(Pageable pageable) {
		cityRepository.findAll();
		return cityRepository.findAll(pageable);
	}

	@PostMapping("/api/v1/cities")
	public City createCity(@Valid @RequestBody City city) {
		return cityRepository.save(city);
	}

	@PutMapping("/api/v1/cities/{cityId}")
	public City updateCity(@PathVariable Long cityId, @Valid @RequestBody City cityRequest) {
		return cityRepository.findById(cityId).map(city -> {

			city.setCountry(cityRequest.getCountry());
			city.setDistrict(cityRequest.getDistrict());
			city.setId(cityRequest.getId());
			city.setName(cityRequest.getName());
			city.setPopulation(cityRequest.getPopulation());

			return cityRepository.save(city);
		}).orElseThrow(() -> new ResourceNotFoundException("CityId " + cityId + " not found"));
	}

	@DeleteMapping("/api/v1/cities/{cityId}")
	public ResponseEntity<?> deleteCity(@PathVariable Long cityId) {
		return cityRepository.findById(cityId).map(city -> {
			cityRepository.delete(city);
			return ResponseEntity.ok().build();
		}).orElseThrow(() -> new ResourceNotFoundException("CityId " + cityId + " not found"));
	}

}
