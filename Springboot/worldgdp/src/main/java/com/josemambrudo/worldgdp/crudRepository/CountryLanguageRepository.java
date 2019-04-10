package com.josemambrudo.worldgdp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldgdp.entity.CountryLanguage;

@Repository
public interface CountryLanguageRepository extends CrudRepository<CountryLanguage, Long> {

}
