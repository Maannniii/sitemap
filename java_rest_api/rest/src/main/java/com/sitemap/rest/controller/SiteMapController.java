package com.sitemap.rest.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sitemap.rest.service.SiteMapService;

@RestController
@RequestMapping("/sitemap")
public class SiteMapController {

	@Autowired
	private SiteMapService service;

	@GetMapping(value = { "", "all" })
	public List<Map<String, Object>> allData() {
		return service.allData();
	}

	@GetMapping("/{id}")
	public List<Map<String, Object>> singleDate(@PathVariable("id") int id) {
		return service.singleDate(id);
	}
}
