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

import com.josemambrudo.worldgdp.crudRepository.CountryLanguageRepository;
import com.josemambrudo.worldgdp.entity.CountryLanguage;
import com.josemambrudo.worldgdp.exception.ResourceNotFoundException;

@RestController
public class CountryLanguageRest {

	@Autowired
	private CountryLanguageRepository countryLanguageRepository;

	@GetMapping("/api/v1/countriesLanguages")
	public Page<CountryLanguage> getAllCountryLanguages(Pageable pageable) {
		countryLanguageRepository.findAll();
		return countryLanguageRepository.findAll(pageable);
	}

	@PostMapping("/api/v1/countriesLanguages")
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

	@DeleteMapping("/api/v1/countriesLanguages/{countryLanguageId}")
	public ResponseEntity<?> deleteCountryLanguage(@PathVariable Long countryLanguageId) {
		return countryLanguageRepository.findById(countryLanguageId).map(countryLanguage -> {
			countryLanguageRepository.delete(countryLanguage);
			return ResponseEntity.ok().build();
		}).orElseThrow(() -> new ResourceNotFoundException("CountryLanguageId " + countryLanguageId + " not found"));
	}

}
