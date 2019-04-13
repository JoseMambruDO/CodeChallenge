package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.Country;

@Repository
public interface CountryRepository extends JpaRepository<Country, Long>{

}