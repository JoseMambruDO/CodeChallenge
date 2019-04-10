package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.City;

@Repository
public interface CityRepository extends CrudRepository<City, Long> {}
