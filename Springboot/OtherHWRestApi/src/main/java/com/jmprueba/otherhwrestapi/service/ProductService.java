package com.jmprueba.otherhwrestapi.service;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import com.jmprueba.otherhwrestapi.entity.Category;
import com.jmprueba.otherhwrestapi.entity.Product;
import com.jmprueba.otherhwrestapi.repository.ProductRepository;

@Service
public class ProductService {
	@Autowired
	ProductRepository productRepository;

	public Page<Product> findAll(Pageable pageable) {

		return productRepository.findAll(pageable);
	}

	public Product save(@Valid Product product) {
		return productRepository.save(product);
	}

	public Product updateProduct(Long productId, @Valid Product product) {

		return productRepository.findById(productId).map(productDty -> {

			productDty.setCategory(product.getCategory());
			productDty.setName(product.getName());
			productDty.setDescription(product.getDescription());
			productDty.setCost(product.getCost());
			productDty.setPrice(product.getPrice());
			productDty.setQuantity(product.getQuantity());

			return productRepository.save(productDty);
		}).orElse(null);
	}

	public boolean deleteProduct(Long productId) {

		return productRepository.findById(productId).map(productDty -> {

			productRepository.delete(productDty);

			return !productRepository.existsById((long) productDty.getId());
		}).orElse(false);

	}

	public Long countProduct() {
		return productRepository.count();
	}

	public List<Product> findBydName(String name) {
		return productRepository.findByName(name);
	}
}
