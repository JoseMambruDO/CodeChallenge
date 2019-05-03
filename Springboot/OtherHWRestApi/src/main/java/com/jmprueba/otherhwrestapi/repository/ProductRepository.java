package com.jmprueba.otherhwrestapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.jmprueba.otherhwrestapi.entity.Product;

@RepositoryRestResource
public interface ProductRepository extends JpaRepository<Product, Long> {


	@Query("SELECT c from Product c Where c.name = :name")
	Product findByName(@Param("name") String name);

}
