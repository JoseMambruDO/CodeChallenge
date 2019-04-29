package com.jmprueba.otherhwrestapi.entity;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;

import lombok.Data;

@Entity
@Data
public class Product {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id;

	private String name;

	private String description;
	
	private Integer quantity;
	
	private Double price;
	
	private Double cost;
	
	@OneToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "id", nullable = true)
	private Category category;

}
