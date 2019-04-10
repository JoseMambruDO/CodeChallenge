package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.Country;

@Repository
public interface CountryRepository extends CrudRepository<Country, Long>{

}
