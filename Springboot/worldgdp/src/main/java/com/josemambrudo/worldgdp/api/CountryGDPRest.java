package com.josemambrudo.worldgdp.api;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.josemambrudo.worldgdp.crudRepository.CountryGDPRepository;
import com.josemambrudo.worldgdp.entity.CountryGDP;
import com.josemambrudo.worldgdp.exception.ResourceNotFoundException;

@RestController
public class CountryGDPRest {

	@Autowired
	private CountryGDPRepository countryGDPRepository;

	@GetMapping("/api/v1/countriesGDP")
	public Page<CountryGDP> getAllCountryGDPs(Pageable pageable) {
		countryGDPRepository.findAll();
		return countryGDPRepository.findAll(pageable);
	}

	@PostMapping("/api/v1/countriesGDP")
	public CountryGDP createCountryGDP(@Valid @RequestBody CountryGDP countryGDP) {
		return countryGDPRepository.save(countryGDP);
	}

	@PutMapping("/api/v1/countriesGDP/{countryGDPId}")
	public CountryGDP updateCountryGDP(@PathVariable Long countryGDPId, @Valid @RequestBody CountryGDP countryGDPRequest) {
		return countryGDPRepository.findById(countryGDPId).map(countryGDP -> {

			countryGDP.setCountry(countryGDPRequest.getCountry());
			countryGDP.setId(countryGDPRequest.getId());
			countryGDP.setVal(countryGDPRequest.getVal());
			countryGDP.setYear(countryGDPRequest.getYear());

			return countryGDPRepository.save(countryGDP);
		}).orElseThrow(() -> new ResourceNotFoundException("CountryGDPId " + countryGDPId + " not found"));
	}

	@DeleteMapping("/api/v1/countryGDP/{countryGDPId}")
	public ResponseEntity<?> deleteCountryGDP(@PathVariable Long countryGDPId) {
		return countryGDPRepository.findById(countryGDPId).map(countryGDP -> {
			countryGDPRepository.delete(countryGDP);
			return ResponseEntity.ok().build();
		}).orElseThrow(() -> new ResourceNotFoundException("CountryGDPId " + countryGDPId + " not found"));
	}

}
