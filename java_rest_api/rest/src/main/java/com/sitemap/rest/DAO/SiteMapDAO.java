package com.sitemap.rest.DAO;

import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.Map;

import org.codehaus.jackson.map.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
public class SiteMapDAO {

	@Autowired
	protected JdbcTemplate jdbc;

	private List<Map<String, Object>> desSerializetoObject(List<Map<String, Object>> list) {
		list.forEach(map -> {
			ObjectMapper objMap = new ObjectMapper();
			try {
				map.put("url", objMap.readValue(map.get("url").toString(), String.class));
				map.put("external_urls", objMap.readValue(map.get("external_urls").toString(), List.class));
				map.put("static_urls", objMap.readValue(map.get("static_urls").toString(), List.class));
				map.put("urls", objMap.readValue(map.get("urls").toString(), List.class));
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		});
		return list;
	}

	public List<Map<String, Object>> allData() {
		String sql = "Select * from sitemap";
		return desSerializetoObject(jdbc.queryForList(sql));
	}

	public List<Map<String, Object>> singleDate(int id) {
		if (id < 1)
			return Collections.emptyList();
		String sql = "Select * from sitemap where id=?";
		return desSerializetoObject(jdbc.queryForList(sql, new Object[] { id }));
	}
}
