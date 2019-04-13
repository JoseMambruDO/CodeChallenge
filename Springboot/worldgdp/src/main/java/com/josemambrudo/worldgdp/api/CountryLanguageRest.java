package com.josemambrudo.worldgdp.api;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.josemambrudo.worldgdp.crudRepository.CountryLanguageRepository;
import com.josemambrudo.worldgdp.entity.CountryLanguage;

import com.josemambrudo.worldgdp.exception.*;

import javax.validation.Valid;

@RestController
public class CountryLanguageRest {

	@Autowired
	private CountryLanguageRepository countryLanguageRepository;

	@GetMapping("/api/v1/countries")
	public Page<CountryLanguage> getAllCountryLanguages(Pageable pageable) {
		countryLanguageRepository.findAll();
		return countryLanguageRepository.findAll(pageable);
	}

	@PostMapping("/api/v1/countries")
	public CountryLanguage createCountryLanguage(@Valid @RequestBody CountryLanguage countryLanguage) {
		return countryLanguageRepository.save(countryLanguage);
	}

	@PutMapping("/api/v1/countries/{countryLanguageId}")
	public CountryLanguage updateCountryLanguage(@PathVariable Long countryLanguageId, @Valid @RequestBody CountryLanguage countryLanguageRequest) {
		return countryLanguageRepository.findById(countryLanguageId).map(countryLanguage -> {

			countryLanguage.setCountry(countryLanguageRequest.getCountry());
			countryLanguage.setId(countryLanguageRequest.getId());
			countryLanguage.setIsOfficial(countryLanguageRequest.getIsOfficial());
			countryLanguage.setPercentage(countryLanguageRequest.getPercentage());
			countryLanguage.setLanguage(countryLanguageRequest.getLanguage());

			return countryLanguageRepository.save(countryLanguage);
		}).orElseThrow(() -> new ResourceNotFoundException("CountryLanguageId " + countryLanguageId + " not found"));
	}

	@DeleteMapping("/countryLanguages/{countryLanguageId}")
	public ResponseEntity<?> deleteCountryLanguage(@PathVariable Long countryLanguageId) {
		return countryLanguageRepository.findById(countryLanguageId).map(countryLanguage -> {
			countryLanguageRepository.delete(countryLanguage);
			return ResponseEntity.ok().build();
		}).orElseThrow(() -> new ResourceNotFoundException("CountryLanguageId " + countryLanguageId + " not found"));
	}

}
