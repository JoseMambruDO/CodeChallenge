package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.City;

@Repository
public interface CityRepository extends JpaRepository<City, Long> {

	
	@Query("SELECT c from City c Where c.name = :name")
	City getCities(@Param("name") String name);

}
