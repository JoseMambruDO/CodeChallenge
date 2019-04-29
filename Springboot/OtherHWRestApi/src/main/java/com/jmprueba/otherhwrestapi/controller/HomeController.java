package com.jmprueba.otherhwrestapi.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

		@GetMapping({"/","index"})
		String home() {
			return "index";
		}
		
}
