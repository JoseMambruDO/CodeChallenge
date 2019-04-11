package com.josemambrudo.worldgdp.entity;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.validation.constraints.NotNull;

import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;

import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Data
@Setter
@Getter
@NoArgsConstructor
@Entity
public class CountryLanguage {
	@Id
	@NotNull
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;

	@ManyToOne(fetch = FetchType.LAZY, optional = false)
	@JoinColumn(name = "country_id", nullable = false)
	@OnDelete(action = OnDeleteAction.CASCADE)
    private Country country;
    private String language;
    private String isOfficial;
    private Double percentage;
    
    
	public CountryLanguage(@NotNull Long id, Country country, String language, String isOfficial, Double percentage) {
		super();
		this.id = id;
		this.country = country;
		this.language = language;
		this.isOfficial = isOfficial;
		this.percentage = percentage;
	}
    
    
    
}
