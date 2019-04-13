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

import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Data
@Getter
@Setter
@NoArgsConstructor
@Entity
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
	@Column(name="countryname")
	private String countryName;
	@NotNull
	private String continent;
	@NotNull
	@Size(max = 26)
	private String region;
	
	@NotNull
	@Column(name="surfacearea")
	private Double surfaceArea;

	@Column(name="indepyear")
	private Short indepYear;

	@NotNull
	private Long population;
	

	@Column(name="lifeexpectancy")
	private Double lifeExpectancy;
	
	private Double gnp;
	
	@NotNull
	@Column(name="localname")
	private String localName;
	
	@NotNull
	@Column(name="governmentform")
	private String governmentForm;
	
	@Column(name="headofstate")
	private String headOfState;
	
	@OneToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "id", nullable = true)
	private City capital;
	
	@NotNull
	private String code2;
	
	public Country(@NotNull Long id, @NotNull @Size(max = 3, min = 3) String code, @NotNull @Size(max = 52) String countryName,
			@NotNull String continent, @NotNull @Size(max = 26) String region, @NotNull Double surfaceArea,
			Short indepYear, @NotNull Long population, Double lifeExpectancy, Double gnp, @NotNull String localName,
			@NotNull String governmentForm, String headOfState, City capital, @NotNull String code2) {
		super();
		this.id = id;
		this.code = code;
		this.countryName = countryName;
		this.continent = continent;
		this.region = region;
		this.surfaceArea = surfaceArea;
		this.indepYear = indepYear;
		this.population = population;
		this.lifeExpectancy = lifeExpectancy;
		this.gnp = gnp;
		this.localName = localName;
		this.governmentForm = governmentForm;
		this.headOfState = headOfState;
		this.capital = capital;
		this.code2 = code2;
	}
	
	
	
	
}
