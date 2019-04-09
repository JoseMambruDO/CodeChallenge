package com.josemambrudo.worldbgp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldbgp.entity.CountryGDP;

@Repository
public interface CountryGDPRepository extends CrudRepository<CountryGDP, Long>{

}
