package com.jmprueba.otherhwrestapi.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

import com.jmprueba.otherhwrestapi.entity.Product;

@RepositoryRestResource
public interface ProductRepository extends JpaRepository<Product, Long> {

	@Query("SELECT p from Product p Where lower(p.name) LIKE CONCAT('%',lower(:name),'%')")
	List<Product> findByName(@Param("name") String name);

}
