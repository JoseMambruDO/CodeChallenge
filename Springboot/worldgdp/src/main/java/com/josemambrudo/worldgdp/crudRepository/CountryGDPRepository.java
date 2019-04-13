package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.CountryGDP;

@Repository
public interface CountryGDPRepository extends JpaRepository<CountryGDP, Long> {

}
