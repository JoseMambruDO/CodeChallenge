package com.jmprueba.otherhwrestapi.api;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.rest.webmvc.ResourceNotFoundException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.jmprueba.otherhwrestapi.entity.Product;
import com.jmprueba.otherhwrestapi.service.ProductService;

@RestController
public class ProductRest {

	@Autowired
	ProductService productService;

	@GetMapping("/api/v1/products")
	public Page<Product> getAllProducts(Pageable pageable) {
		return productService.findAll(pageable);
	}

	@PostMapping("/api/v1/products")
	public Product createProduct(@Valid @RequestBody Product product) {
		return productService.save(product);
	}

	@PutMapping("/api/v1/products/{ProductId}")
	public Product updateProduct(@PathVariable Long productId, @Valid @RequestBody Product product) {
		Product productUpdated = productService.updateProduct(productId, product);
		if (productUpdated == null)
			throw new ResourceNotFoundException("Product Id " + productId + " not found");
		return productUpdated;
	}

	@DeleteMapping("/api/v1/products/{ProductId}")
	public ResponseEntity<?> deleteProduct(@PathVariable Long productId) {

		if (!productService.deleteProduct(productId))
			throw new ResourceNotFoundException("Product Id " + productId + " not found");

		return ResponseEntity.ok().build();

	}

	@GetMapping("/api/v1/products/count")
	public Long countProduct() {
		return productService.countProduct();
	}

}
