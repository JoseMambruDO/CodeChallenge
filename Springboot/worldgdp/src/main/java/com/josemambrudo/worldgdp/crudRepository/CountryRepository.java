package com.josemambrudo.worldgdp.crudRepository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.Country;

@Repository
public interface CountryRepository extends JpaRepository<Country, Long>{

	@Query("SELECT c from Country c Where c.countryName = :countryName")
	Country findByCountryName(@Param("countryName") String countryName);

	@Query("SELECT DISTINCT c.region from Country c")
	List<String> getRegions();
	
	@Query("SELECT DISTINCT c.continent from Country c")
	List<String> getContinents();
}
