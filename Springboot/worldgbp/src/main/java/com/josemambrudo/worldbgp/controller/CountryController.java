package com.josemambrudo.worldbgp.controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class CountryController {

	@GetMapping("/")
	public String main() {
		return "index";
	}
}
