import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class BloodGlucoseScreen extends StatefulWidget {
  @override
  _BloodGlucoseScreenState createState() => _BloodGlucoseScreenState();
}

class _BloodGlucoseScreenState extends State<BloodGlucoseScreen> {
  TextEditingController _controller = TextEditingController();
  List<int> _glucoseLevels = [];

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  // Load saved glucose levels from shared preferences
  _loadData() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    List<String>? savedLevels = prefs.getStringList('glucoseLevels');
    if (savedLevels != null) {
      _glucoseLevels = savedLevels.map((e) => int.parse(e)).toList();
    }
    setState(() {});
  }

  // Save glucose levels to shared preferences
  _saveData() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    List<String> stringList = _glucoseLevels.map((e) => e.toString()).toList();
    prefs.setStringList('glucoseLevels', stringList);
  }

  // Handle glucose level submission
  _submitGlucoseLevel() {
    if (_controller.text.isNotEmpty) {
      setState(() {
        _glucoseLevels.add(int.parse(_controller.text));
      });
      _saveData();
      _controller.clear();
    }
  }

  // Generate line chart data
  List<charts.Series<GlucoseData, int>> _generateLineChartData() {
    // Prepare data for the chart
    List<GlucoseData> data = _glucoseLevels.asMap().entries.map((entry) {
      int index = entry.key;
      int level = entry.value;
      return GlucoseData(index + 1, level); // Index + 1 to represent the day
    }).toList();

    return [
      charts.Series<GlucoseData, int>(
        id: 'Glucose Levels',
        data: data,
        domainFn: (GlucoseData glucoseData, _) => glucoseData.day,
        measureFn: (GlucoseData glucoseData, _) => glucoseData.level,
        colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
      ),
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Blood Glucose Tracker")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Input field for glucose level
            TextField(
              controller: _controller,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: "Enter Blood Glucose Level",
                border: OutlineInputBorder(),
              ),
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: _submitGlucoseLevel,
              child: Text("Add Glucose Level"),
            ),
            SizedBox(height: 32),
            ElevatedButton(
              onPressed: () {
                // Navigate to a new screen for the line chart report
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) =>
                        ReportScreen(glucoseLevels: _glucoseLevels),
                  ),
                );
              },
              child: Text("Generate Report"),
            ),
            SizedBox(height: 32),
            // Display all entered glucose levels
            Expanded(
              child: ListView.builder(
                itemCount: _glucoseLevels.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(
                        'Day ${index + 1}: ${_glucoseLevels[index]} mg/dL'),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class ReportScreen extends StatelessWidget {
  final List<int> glucoseLevels;

  ReportScreen({required this.glucoseLevels});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Blood Glucose Report")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              height: 500,
              width: 500,
              child: charts.LineChart(
                _generateLineChartData(),
                animate: true,
                defaultRenderer: charts.LineRendererConfig(
                  includeArea: true,
                  areaOpacity: 0.3,
                  strokeWidthPx: 2,
                ),
                primaryMeasureAxis: charts.NumericAxisSpec(
                  tickProviderSpec:
                      charts.BasicNumericTickProviderSpec(desiredTickCount: 5),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // Generate line chart data for report
  List<charts.Series<GlucoseData, int>> _generateLineChartData() {
    List<GlucoseData> data = glucoseLevels.asMap().entries.map((entry) {
      int index = entry.key;
      int level = entry.value;
      return GlucoseData(index + 1, level); // Index + 1 to represent the day
    }).toList();

    return [
      charts.Series<GlucoseData, int>(
        id: 'Glucose Levels',
        data: data,
        domainFn: (GlucoseData glucoseData, _) => glucoseData.day,
        measureFn: (GlucoseData glucoseData, _) => glucoseData.level,
        colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
      ),
    ];
  }
}

class GlucoseData {
  final int day;
  final int level;

  GlucoseData(this.day, this.level);
}
