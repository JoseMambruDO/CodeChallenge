package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.CountryLanguage;

@Repository
public interface CountryLanguageRepository extends JpaRepository<CountryLanguage, Long> {

}
