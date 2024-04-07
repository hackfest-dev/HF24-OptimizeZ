import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import 'const.dart';

class ImageScreen extends StatefulWidget {
  @override
  _ImageScreenState createState() => _ImageScreenState();
}

class _ImageScreenState extends State<ImageScreen> {
  List<Container> imageContainers = [];
  Map<String, dynamic> woundData = {};

  @override
  void initState() {
    super.initState();
    fetchImages();
    fetchWoundData();
  }



Future<void> fetchWoundData() async {
  try {
    final response = await http.get(Uri.parse('http://192.168.137.26:5000/get_output_json'));
    if (response.statusCode == 200) {
      woundData = json.decode(response.body);
      setState(() {});
    } else {
      print('Failed to fetch wound data: ${response.statusCode}');
    }
  } catch (e) {
    print('Error fetching wound data: $e');
  }
} Future<void> fetchImages() async {
    try {
      final response =
          await http.get(Uri.parse('http://192.168.137.26:5000/getres'));
      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);
        data.forEach((key, value) {
          var image = Image.memory(
            base64Decode(value),
            fit: BoxFit.fill,
          );
          var container = Container(
            margin: EdgeInsets.all(10),
            height: 200,
            width: 200,
            child: image,
          );
          imageContainers.add(container);
        });
        setState(() {});
      } else {
        print('Failed to fetch images: ${response.statusCode}');
      }
    } catch (e) {
      print('Error fetching images: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        iconTheme: IconThemeData(color: Colors.white),
        backgroundColor: Color(kbluepastle),
        title: Text(
          'Result Screens',
          style: TextStyle(color: Colors.white),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: ListView(
          children: [
            Container(
              height: 500,
              child: GridView.builder(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2),
                itemCount: imageContainers.length,
                itemBuilder: (context, index) {
                  return imageContainers[index];
                },
              ),
            ),
            Card(
              child: Padding(
                padding: const EdgeInsets.all(10.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text("Wound Data", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                    SizedBox(height: 10),
                    Text("Area: ${woundData['area'] ?? ''}mm square"),
                    Text("Height: ${woundData['h'] ?? ''}mm"),
                    Text("Width: ${woundData['w'] ?? ''}mm"),
                    Text("Type: ${woundData['woundType'] ?? ''}"),
                    Text("Severity: ${woundData['severity'] ?? ''}"),
                    Text("Estimated Healing Time: ${woundData['healingTime'] ?? ''}Days"),
                  ],
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
