package com.josemambrudo.worldbgp.entity;

import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.springframework.data.annotation.Id;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Getter
@Setter
public class Country {
	@Id
	@NotNull
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;
	
	@NotNull
	@Size(max = 3, min = 3)
	private String code;
	@NotNull
	@Size(max = 52)
	private String name;
	@NotNull
	private String continent;
	@NotNull
	@Size(max = 26)
	private String region;
	@NotNull
	private Double surfaceArea;
	private Short indepYear;
	@NotNull
	private Long population;
	private Double lifeExpectancy;
	private Double gnp;
	@NotNull
	private String localName;
	@NotNull
	private String governmentForm;
	private String headOfState;
	private City capital;
	@NotNull
	private String code2;
}