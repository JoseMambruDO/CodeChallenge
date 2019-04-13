package com.josemambrudo.worldgdp.api;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.josemambrudo.worldgdp.crudRepository.CountryRepository;
import com.josemambrudo.worldgdp.entity.Country;

import com.josemambrudo.worldgdp.exception.*;

import javax.validation.Valid;

@RestController
public class CountryRest {

	@Autowired
	private CountryRepository countryRepository;

	@GetMapping("/api/v1/countries")
	public Page<Country> getAllCountrys(Pageable pageable) {
		countryRepository.findAll();
		return countryRepository.findAll(pageable);
	}

	@PostMapping("/api/v1/countries")
	public Country createCountry(@Valid @RequestBody Country country) {
		return countryRepository.save(country);
	}

	@PutMapping("/api/v1/countries/{countryId}")
	public Country updateCountry(@PathVariable Long countryId, @Valid @RequestBody Country countryRequest) {
		return countryRepository.findById(countryId).map(country -> {

			country.setCode(countryRequest.getCode());
			country.setCode2(countryRequest.getCode2());
			country.setContinent(countryRequest.getContinent());
			country.setCapital(countryRequest.getCapital());
			country.setGnp(countryRequest.getGnp());
			country.setGovernmentForm(countryRequest.getGovernmentForm());
			country.setHeadOfState(countryRequest.getHeadOfState());
			country.setId(countryRequest.getId());
			country.setIndepYear(countryRequest.getIndepYear());
			country.setLifeExpectancy(countryRequest.getLifeExpectancy());
			country.setLocalName(countryRequest.getLocalName());
			country.setPopulation(countryRequest.getPopulation());
			country.setRegion(countryRequest.getRegion());
			country.setSurfaceArea(countryRequest.getSurfaceArea());

			return countryRepository.save(country);
		}).orElseThrow(() -> new ResourceNotFoundException("CountryId " + countryId + " not found"));
	}

	@DeleteMapping("/countrys/{countryId}")
	public ResponseEntity<?> deleteCountry(@PathVariable Long countryId) {
		return countryRepository.findById(countryId).map(country -> {
			countryRepository.delete(country);
			return ResponseEntity.ok().build();
		}).orElseThrow(() -> new ResourceNotFoundException("CountryId " + countryId + " not found"));
	}

}
