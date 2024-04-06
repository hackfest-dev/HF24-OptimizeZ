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

  @override
  void initState() {
    super.initState();
    fetchImages();
  }

  Future<void> fetchImages() async {
    try {
      final response =
          await http.get(Uri.parse('http://192.168.137.163:5000/getres'));
      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);
        data.forEach((key, value) {
          var image = Image.memory(
            base64Decode(value),
            fit: BoxFit.fill,
          );
          var container = Container(
            //  color: Colors.amber,
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
          'Selected Image',
          style: TextStyle(color: Colors.white),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          children: [
            Container(
              height: 400,
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
              child: Center(
                child: Container(
                  height: 200,
                  width: 200,
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Wound Area"),
                      Text("Wound height"),
                      Text("Wound Width"),
                      Text("Wound Type"),
                      Text("Sevarity"),
                      Text("Estimated Healing Time:")
                    ],
                  ),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
