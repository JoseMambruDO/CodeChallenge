package com.jmprueba.otherhwrestapi.entity;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.hibernate.validator.constraints.Length;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@NoArgsConstructor
@JsonIgnoreProperties({ "hibernateLazyInitializer", "handler" })
public class Product {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@ApiModelProperty(notes = "ID generate by database sequence")
	private Long id;

	@NotNull
	@ApiModelProperty(notes = "Name producto")
	private String name;

	@ApiModelProperty(notes = "Detail of product")
	private String description;

	@Min(0)
	@ApiModelProperty(notes = "Quantity avaiable of product on store")
	private Integer quantity;

	@Min(0)
	@ApiModelProperty(notes = "Price of selling")
	private Double price;

	@Min(0)
	@ApiModelProperty(notes = "Cost for buying")
	private Double cost;

	@ManyToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "category_id", nullable = false)
	@ApiModelProperty(notes = "Category of product classification")
	private Category category;

}
