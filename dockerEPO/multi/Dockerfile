# build
FROM golang:1.23
WORKDIR /src
COPY <<EOF /src/main.go
package main
import "fmt"
func main() {
  fmt.Println("hello, world") }
EOF
RUN go build -o /bin/hello ./main.go

# run program
CMD ["/bin/hello"]
