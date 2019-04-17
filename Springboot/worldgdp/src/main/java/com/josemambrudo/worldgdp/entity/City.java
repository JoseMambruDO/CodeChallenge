package com.josemambrudo.worldgdp.entity;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
public class City {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
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
	
	
}
