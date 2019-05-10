package com.jmprueba.otherhwrestapi.api;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.rest.webmvc.ResourceNotFoundException;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.jmprueba.otherhwrestapi.entity.Category;
import com.jmprueba.otherhwrestapi.service.CategoryService;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

import springfox.documentation.spring.web.json.Json;


@RestController
@Api("Category RestAPI")
@RequestMapping("/api/v1/categories")
public class CategoryRest {

	@Autowired
	CategoryService categoryService;
	@ApiOperation(value = "Get all category avaiable.")
	@GetMapping
	public Page<Category> getAllCategories(Pageable pageable) {
		return categoryService.findAll(pageable);
	}
	@ApiOperation(value = "Get a list of category by part of name.")
	@GetMapping("findByName/{name}")
	public List<Category> getAllCategories(@PathVariable String name) {
		return categoryService.findByName(name);
	}
	@ApiOperation(value = "Get a category by Id.")
	@GetMapping("findByID/{id}")
	public Category getCategoryByID(@PathVariable Long id) {
		return categoryService.findById(id);
	}
	@ApiOperation(value = "Add a category.")
	@PostMapping
	public Category createCategory(@Valid @RequestBody Category category) {
		return categoryService.save(category);
	}

	@ApiOperation(value = "Edit a category.")
	@PutMapping("{id}")
	public Category updateCategory(@PathVariable Long id, @Valid @RequestBody Category category) {
		Category categoryUpdated = categoryService.updateCategory(id, category);
		if (categoryUpdated == null)
			throw new ResourceNotFoundException("Category id " + id + " not found");
		return categoryUpdated;
	}
	
	@ApiOperation(value = "Delete a category")

	@DeleteMapping("{id}")
	public String deleteCategory(@PathVariable Long id) {

		if (!categoryService.deleteCategory(id))
			throw new ResourceNotFoundException("Category id " + id + " not found");
		return String.format("Category id:%d was deleted.", id);
	}

	@ApiOperation(value = "Count avaiable category")
	@GetMapping("count")
	public Long countCategory() {
		return categoryService.countCategory();
	}

}
