package com.josemambrudo.worldbgp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldbgp.entity.Country;

@Repository
public interface CountryRepository extends CrudRepository<Country, Long>{

}
