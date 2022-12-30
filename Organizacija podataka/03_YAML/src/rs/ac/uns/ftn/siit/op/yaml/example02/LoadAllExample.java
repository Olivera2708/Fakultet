package rs.ac.uns.ftn.siit.op.yaml.example02;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.databind.ObjectMapper;

public class LoadAllExample {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws FileNotFoundException {
		try (InputStream input = new FileInputStream(new File("resources/log.yaml"));) {

			Yaml yaml = new Yaml();
			int counter = 0;

			// The .loadAll(input) method returns an instance of Iterable<Object>,
			// where each object is of type Map<String, Object>
			for (Object data : yaml.loadAll(input)) {

				Map<String, Object> dataMap = (Map<String, Object>) data;
				System.out.println("Time: " + dataMap.get("Time"));

				counter++;
				ObjectMapper mapper = new ObjectMapper();
				mapper.writeValue(new FileWriter("resources/jsonsjon.json", true), dataMap);
			}
			

			System.out.println("No. of documents: " + counter);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
