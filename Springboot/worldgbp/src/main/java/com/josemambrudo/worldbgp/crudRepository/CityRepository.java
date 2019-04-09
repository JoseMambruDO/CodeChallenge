package com.josemambrudo.worldbgp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldbgp.entity.City;

@Repository
public interface CityRepository extends CrudRepository<City, Long> {}