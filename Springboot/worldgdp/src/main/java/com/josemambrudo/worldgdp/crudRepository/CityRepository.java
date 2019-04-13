package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.City;

@Repository
public interface CityRepository extends JpaRepository<City, Long> {
}
