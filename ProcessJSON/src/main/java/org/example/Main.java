package org.example;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static JSONArray readJSON(String filePath) throws IOException, ParseException {
        JSONParser parser = new JSONParser();
        JSONArray data = (JSONArray) parser.parse(new FileReader(filePath));
        return data;
    }

    public static void main(String[] args) throws IOException, ParseException {
        String filePath = "input.json";
        JSONArray data = readJSON(filePath);
        System.out.println("data");
        System.out.println(data);
        JSONArray processedData = processJSON(data);
        System.out.println("processedData");
        System.out.println(processedData);
    }


    private static JSONArray processJSON(JSONArray data) {

        for(int i=0; i<data.size(); i++){
            JSONObject entry = (JSONObject)data.get(i);
            entry.put("name", entry.get("first_name")+" "+entry.get("last_name"));
            entry.remove("first_name");
            entry.remove("last_name");
        }
        return data;
    }
}