package com.jmprueba.otherhwrestapi.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

		@GetMapping({"/","index","product"})
		String home() {
			return "index";
		}

		@GetMapping({"category"})
		String product() {
			return "category";
		}

}
