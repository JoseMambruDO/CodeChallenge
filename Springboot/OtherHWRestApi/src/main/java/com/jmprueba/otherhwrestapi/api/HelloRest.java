package com.jmprueba.otherhwrestapi.api;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController

public class HelloRest {
	
	@RequestMapping("/api/hello")
    String hello() 
    {
        return "Hello World :: ok";
    }

}
