package com.josemambrudo.worldbgp.crudRepository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.josemambrudo.worldbgp.entity.CountryLanguage;

@Repository
public interface CountryLanguageRepository extends CrudRepository<CountryLanguage, Long> {

}
