package com.josemambrudo.worldgdp.controller;


import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

import com.josemambrudo.worldgdp.crudRepository.CityRepository;
import com.josemambrudo.worldgdp.crudRepository.CountryRepository;


@Controller
public class CountryController {

	@Autowired
	CountryRepository countryRepository;
	
	@Autowired
	CityRepository cityRepository;
	
	
	@GetMapping({"/countries","/"})
	public String countries(Model model, 
		@RequestParam Map<String, Object> params
	) {
		model.addAttribute("continents", countryRepository.getContinents());
		model.addAttribute("regions", countryRepository.getRegions());
		model.addAttribute("countries", countryRepository.findAll());
		model.addAttribute("count", countryRepository.count());
		return "countries";
	}
	

	@GetMapping("/countries/{code}")
	public String countryDetail(@PathVariable String code, Model model) {
		model.addAttribute("c", countryRepository.getCountryByCode(code));
		return "country";
	}
	
	@GetMapping("/countries/{code}/form")
	public String editCountry(@PathVariable String code, Model model) {
		model.addAttribute("c", countryRepository.getCountryByCode(code));
		model.addAttribute("cities", cityRepository.getCities(code));
		model.addAttribute("continents", countryRepository.getContinents());
		model.addAttribute("regions", countryRepository.getRegions());
		model.addAttribute("heads", countryRepository.getHeadOfStates());
		model.addAttribute("govs", countryRepository.getGovernmentTypes());
		return "country-form";
	}
	
}
