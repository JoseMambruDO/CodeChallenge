package com.jmprueba.otherhwrestapi.service;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import com.jmprueba.otherhwrestapi.entity.Category;
import com.jmprueba.otherhwrestapi.repository.CategoryRepository;

@Service
public class CategoryService {
	@Autowired
	CategoryRepository categoryRepository;

	public Page<Category> findAll(Pageable pageable) {

		return categoryRepository.findAll(pageable);
	}

	public Category findBydName(String name) {
		return categoryRepository.findByName(name);
	}

	
	public Category save(@Valid Category category) {
		return categoryRepository.save(category);
	}

	public Category updateCategory(Long categoryId, @Valid Category category) {

		return categoryRepository.findById(categoryId).map(categoryDty -> {

			categoryDty.setName(category.getName());

			return categoryRepository.save(categoryDty);
		}).orElse(null);
	}

	public boolean deleteCategory(Long categoryId) {

		return categoryRepository.findById(categoryId).map(categoryDty -> {

			categoryRepository.delete(categoryDty);

			return !categoryRepository.existsById((long) categoryDty.getId());
		}).orElse(false);

	}

	public Long countCategory() {
		return categoryRepository.count();
	}

	
}
