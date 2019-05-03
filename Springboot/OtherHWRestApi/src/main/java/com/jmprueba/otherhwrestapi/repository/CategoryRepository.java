package com.jmprueba.otherhwrestapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.jmprueba.otherhwrestapi.entity.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {

	@Query("SELECT c from Category c Where c.name = :name")
	Category findByName(@Param("name") String name);
}
