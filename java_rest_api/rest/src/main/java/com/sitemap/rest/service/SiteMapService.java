package com.sitemap.rest.service;

import java.util.Collections;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sitemap.rest.DAO.SiteMapDAO;

@Service
public class SiteMapService {
	@Autowired
	private SiteMapDAO dao;

	public List<Map<String, Object>> allData() {
		return dao.allData();
	}

	public List<Map<String, Object>> singleDate(int id) {
		if (id < 1)
			return Collections.emptyList();
		return dao.singleDate(id);
	}

}
