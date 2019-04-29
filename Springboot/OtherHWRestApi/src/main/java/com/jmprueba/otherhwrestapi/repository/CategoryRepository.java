package com.jmprueba.otherhwrestapi.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.jmprueba.otherhwrestapi.entity.Category;

public interface CategoryRepository extends JpaRepository<Category, Long> {

}
