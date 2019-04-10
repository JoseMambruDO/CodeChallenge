package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.CountryGDP;

@Repository
public interface CountryGDPRepository extends CrudRepository<CountryGDP, Long>{

}
