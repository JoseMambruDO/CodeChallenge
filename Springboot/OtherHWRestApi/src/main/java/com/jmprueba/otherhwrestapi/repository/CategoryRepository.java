package com.jmprueba.otherhwrestapi.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.jmprueba.otherhwrestapi.entity.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {

	@Query("SELECT c from Category c Where lower(c.name) LIKE CONCAT('%',lower(:name),'%')")
	List<Category> findByName(@Param("name") String name);
}
