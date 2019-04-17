package com.josemambrudo.worldgdp;


import static org.assertj.core.api.Assertions.assertThat;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase.Replace;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;
import org.springframework.test.context.junit4.SpringRunner;

import com.josemambrudo.worldgdp.crudRepository.CountryRepository;
import com.josemambrudo.worldgdp.entity.Country;

@RunWith(SpringRunner.class)
@DataJpaTest
@AutoConfigureTestDatabase(replace=Replace.NONE)
public class CountryRepositoryIntegrationTest {

	@Autowired
	private CountryRepository countryRepository;

	@Autowired
	private TestEntityManager entityManager;

	@Test
	public void whenFindByName_thenReturnCountry() {

		// given
		Country DRCountry = new Country();

		DRCountry.setCode("RDO");
		DRCountry.setCode2("SDO");
		DRCountry.setContinent("South America");
		DRCountry.setCountryName("Dominican Republic");
		DRCountry.setGnp(96.53294);
		DRCountry.setGovernmentForm("Republica Democratica");
		DRCountry.setHeadOfState("");
		DRCountry.setIndepYear((short) 1844);
		DRCountry.setLifeExpectancy((short) 1844);
		DRCountry.setLocalName("Republica Dominicana");
		DRCountry.setRegion("Antillas Mayores");
		DRCountry.setPopulation((long) 10_770_909);
		DRCountry.setSurfaceArea((double) 48440);

		entityManager.persist(DRCountry);
		entityManager.flush();

		// when
		Country found = countryRepository.findByCountryName(DRCountry.getCountryName());

		// then
		assertThat(found.getCountryName()).isEqualTo(DRCountry.getCountryName());
	}
}
