package com.josemambrudo.worldgdp.entity;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@Data
@NoArgsConstructor
@Entity
public class City {
	@Id
	@NotNull
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;
	@NotNull
	@Size(max = 35)
	private String name;
	
	@ManyToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "country_id", nullable = false)
	@OnDelete(action = OnDeleteAction.CASCADE)
	private Country country;
	@NotNull
	@Size(max = 20)
	private String district;
	@NotNull
	private Long population;
	
	
	public City(@NotNull Long id, @NotNull @Size(max = 35) String name, Country country,
			@NotNull @Size(max = 20) String district, @NotNull Long population) {
		super();
		this.id = id;
		this.name = name;
		this.country = country;
		this.district = district;
		this.population = population;
	}
	
	
}
