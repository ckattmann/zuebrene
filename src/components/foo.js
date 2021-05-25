
			// Jan 1 2019 UTC
			let start = 1546300800;
			let times = [];

			for (let h = 0; h < 365 * 24; h++)
				times.push(start + h * 3600);

			let values = Array(times.length);

			for (let i = 0; i < times.length; i++)
				values[i] = i % 24 == 0 ? 1 : 0.5;

			let data0 = [
				times,
				values,
			];

			function sliceRange(fromTs, numDays) {
				return [
					times.slice(fromTs, fromTs + 24 * numDays),
					values.slice(fromTs, fromTs + 24 * numDays),
				];
			}

			function putHeader(text) {
				let h = document.createElement("h3");
				h.textContent = text;
				document.body.appendChild(h);
			}

			function genOpts(title, tz, syncKey) {
				return {
					title: title,
					tzDate: ts => uPlot.tzDate(new Date(ts * 1e3), tz),
					cursor: {
						sync: {
							key: syncKey,
							setSeries: true,
						},
					},
					width: 600,
					height: 300,
					series: [
						{},
						{
							label: "2019",
							stroke: "red",
						},
					],
				}
			}

			let data;


			putHeader('London\'s 2019 "spring forward" time range');
			data = sliceRange(times.findIndex(v => v == 1553774400), 6);
			syncKey = 0;

			new uPlot(
				genOpts("UTC (no DST)", 'Etc/UTC', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("Europe/London (Mar 31, 2019: 1am -> 2am)", 'Europe/London', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("America/Chicago (no DST switch in this range)", 'America/Chicago', syncKey),
				data,
				document.body
			);


			putHeader('London\'s 2019 "fall back" time range');
			data = sliceRange(times.findIndex(v => v == 1571918400), 6);
			syncKey = 1;

			new uPlot(
				genOpts("UTC (no DST)", 'Etc/UTC', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("Europe/London (Oct 27, 2019: 2am -> 1am)", 'Europe/London', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("America/Chicago (no DST switch in this range)", 'America/Chicago', syncKey),
				data,
				document.body
			);


			putHeader('Chicago\'s 2019 "spring forward" time range');
			data = sliceRange(times.findIndex(v => v == 1551960000), 6);
			syncKey = 2;

			new uPlot(
				genOpts("UTC (no DST)", 'Etc/UTC', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("America/Chicago (Mar 10, 2019: 2am -> 3am)", 'America/Chicago', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("Europe/London (no DST switch in this range)", 'Europe/London', syncKey),
				data,
				document.body
			);

			putHeader('Chicago\'s 2019 "fall back" time range');
			data = sliceRange(times.findIndex(v => v == 1572523200), 6);
			syncKey = 3;

			new uPlot(
				genOpts("UTC (no DST)", 'Etc/UTC', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("America/Chicago (Nov 3, 2019: 2am -> 1am)", 'America/Chicago', syncKey),
				data,
				document.body
			);

			new uPlot(
				genOpts("Europe/London (no DST switch in this range)", 'Europe/London', syncKey),
				data,
				document.body
			);
		