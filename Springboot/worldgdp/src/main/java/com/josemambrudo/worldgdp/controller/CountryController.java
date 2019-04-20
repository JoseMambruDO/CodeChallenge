package com.josemambrudo.worldgdp.controller;


import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.josemambrudo.worldgdp.crudRepository.CountryRepository;


@Controller
public class CountryController {

	@Autowired
	CountryRepository countryRepository;
	
	@GetMapping("/")
	public String mainController() {
		return "index";
	}
	
	
	@GetMapping({"/countries"})
	public String countries(Model model, 
		@RequestParam Map<String, Object> params
	) {
		model.addAttribute("countries", countryRepository.findAll());
		model.addAttribute("count", countryRepository.count());
	
		return "countries";
	}
	
}
