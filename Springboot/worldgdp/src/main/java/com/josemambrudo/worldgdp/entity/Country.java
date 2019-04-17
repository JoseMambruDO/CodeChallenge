package com.josemambrudo.worldgdp.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
public class Country {
	@Id
	
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	@NotNull
	@Size(max = 3, min = 3)
	private String code;
	@NotNull
	@Size(max = 52)
	@Column(name = "countryname")
	private String countryName;
	@NotNull
	private String continent;
	@NotNull
	@Size(max = 26)
	private String region;

	@NotNull
	@Column(name = "surfacearea")
	private Double surfaceArea;

	@Column(name = "indepyear")
	private Short indepYear;

	@NotNull
	private Long population;

	@Column(name = "lifeexpectancy")
	private Short lifeExpectancy;

	private Double gnp;

	@NotNull
	@Column(name = "localname")
	private String localName;

	@NotNull
	@Column(name = "governmentform")
	private String governmentForm;

	@Column(name = "headofstate")
	private String headOfState;

	@OneToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "id", nullable = true)
	private City capital;

	@NotNull
	private String code2;
}
