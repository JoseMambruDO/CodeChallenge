package com.josemambrudo.worldgdp.entity;

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
	@OneToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "country_id", nullable = false)
	private City capital;
	@NotNull
	private String code2;
	
	public Country(@NotNull Long id, @NotNull @Size(max = 3, min = 3) String code, @NotNull @Size(max = 52) String name,
			@NotNull String continent, @NotNull @Size(max = 26) String region, @NotNull Double surfaceArea,
			Short indepYear, @NotNull Long population, Double lifeExpectancy, Double gnp, @NotNull String localName,
			@NotNull String governmentForm, String headOfState, City capital, @NotNull String code2) {
		super();
		this.id = id;
		this.code = code;
		this.name = name;
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
