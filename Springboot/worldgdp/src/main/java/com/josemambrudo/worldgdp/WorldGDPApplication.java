package com.josemambrudo.worldgdp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication
@EnableJpaRepositories(basePackages = {"com.josemambrudo.worldgdp.entity", "com.josemambrudo.worldgdp.crudRepository"})
public class WorldGDPApplication {

	public static void main(String[] args) {
		SpringApplication.run(WorldGDPApplication.class, args);
	}

}
